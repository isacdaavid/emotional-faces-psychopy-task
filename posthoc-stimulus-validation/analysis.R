## author: Isaac David <isacdaavid@at@isacdaavid@dot@info>
## license: GPLv3 or later

## task-dependent neural data is only as good as stimuli
## allow. stimuli must elicit the adequate behavior and physiological
## phenomena. this script assesses dependence between intended
## stimulus category and subjectively-chosen category by study
## participants, as tested prior to fMRI acquisition.

library(ggplot2)
BASE_SIZE <- 21
theme_set(theme_gray(base_size = BASE_SIZE))

DATA_DIR <- './'
dirs <- list.dirs(DATA_DIR, recursive = FALSE)

## plot contingency/confusion table and perform Pearson's Chi-squared
## dependence test on it. FWER-corrected with Bonferroni
##
## input: df: frequency dataframe, e.g. from freq_dataframe()
##        n_tests: number of comparisons to correct for
## output: ggplot object
plot_conf_matrix <- function(df, n_tests = 1, text_size = 5, nudge_x = 0,
                             angle = 0, x_labels_position = "top",
                             x_labels = c("angry", "happy", "neutral", "sad")) {
    mytest <- chisq.test(xtabs(Frecuencia ~ Respuesta + Realidad, data = df))
    ggplot(df, aes(x = Realidad,
                   y = ordered(Respuesta, levels = rev(levels(Respuesta))))) +
        geom_tile(aes(fill = Frecuencia)) +
        geom_text(data = subset(df, Frecuencia != "0"),
                  aes(label = sprintf("%1d", Frecuencia)),
                  angle = angle,
                  color = "white",
                  vjust = 1,
                  size = text_size,
                  nudge_x = nudge_x) +
        labs(y = "Respuesta",
             title = "Frecuencia conjunta de\ncategorización de estímulos",
             caption = paste0("χ2 de Pearson = ",
                              signif(mytest$statistic, 2),
                              ", gdl = ",
                              signif(mytest$parameter, 2),
                              if (n_tests > 1) ", valor p (Bonferroni) = " else ", valor p = ",
                              signif(mytest$p.value * n_tests, 2))) +
        guides(fill = FALSE) +
        scale_x_discrete(position = x_labels_position, labels = x_labels) +
        theme(axis.text.x = element_text(angle = 90,
                                         hjust = 1,
                                         size = BASE_SIZE * .6))
}

## perform binomial tests on contingency/confusion table
## columns. I.e., compute the probabilities of observing same or
## better categorisation under the hypothesis that subjects are
## randomly guessing, each response being an independent Bernoulli
## trial of probability 1/4. FWER-corrected with Holm's method.
##
## input: conf_mat: contingency matrix
## output: Holm-adjusted list of binomial tests
multiple_binomial_tests <- function(conf_mat) {
    ## assume ordered matrix with n*4 columns and specify which row
    ## contains the hits
    conf_mat <- rbind(conf_mat,
                      hits_row = do.call(c, lapply(1:4, function(x) {
                          rep(x, ncol(conf_mat) / 4)
                      })))
    tests <- apply(conf_mat, MARGIN = 2, function(column) {
        binom.test(column[column["hits_row"]],
                   n = sum(column[1:4]),
                   p = 1/4,
                   alternative = "greater")
    })
    corrected_pvals <- p.adjust(unlist(lapply(tests, function(t) t$p.value)),
                                "holm",
                                length(tests))
    ## update tests
    for (i in 1:length(tests)) {
        tests[[i]]$p.value <- corrected_pvals[i]
    }
    return(tests)
}

## transform numeric p-values vector to character vector, emptying
## significant values
##
## input: pvals: vector with p-values
##        thr = .05: cutoff value
## output: character vector with rounded p-values or empty elements, depending
##         on the original value and thr
threshold <- function(pvals, thr = .05) {
    unname(sapply(pvals, function(p) {
        if (p >= thr) as.character(round(p, 2)) else "     "
    }))
}

################################################################################
## per-emotion analysis: how good are subjects (individually and collectively)
##                       at discriminating each intended emotion?
##                       identify problematic emotions and problematic subjects
################################################################################

## transform raw subject responses (as saved by gui.R) into response
## frequency data frame.
##
## input: path to subject directory (character string)
## output: dataframe with columns c("Respuesta", "Realidad", "Frecuencia")
freq_dataframe <- function(dir) {
    data <- read.csv(paste0(dir, '/subject.csv'), sep = '\t')
    conf_mat <- table(data$response, data$emotion)
    df <- as.data.frame(conf_mat)
    colnames(df) <- c("Respuesta", "Realidad", "Frecuencia")
    return(df)
}

main_emotions <- function() {
    ## per-subject frequency dataframes (list of)
    freq_dataframes <- lapply(dirs, freq_dataframe)

    ## collapse into group frequency dataframe
    global_freq_dataframe <-
        cbind(freq_dataframes[[1]][, c("Respuesta", "Realidad")],
              Frecuencia = Reduce(f = "+",
                                  x = lapply(freq_dataframes,
                                             function(df) { df$Frecuencia } )))

    ## per-subject plots, save at subject directories
    lapply(1:length(dirs), function(n) {
        df <- freq_dataframes[[n]]
        x_labels <- threshold(unlist(lapply(
            multiple_binomial_tests(xtabs(Frecuencia ~ Respuesta + Realidad,
                                          data = df)),
            function(t) t$p.value)))
        svg(paste0(dirs[n], '/conf-matrix.svg'))
        plot(plot_conf_matrix(df,
                              n_tests = length(freq_dataframes),
                              x_labels = x_labels))
        dev.off()
    })

    ## group plot
    x_labels <- threshold(unlist(lapply(
        multiple_binomial_tests(xtabs(Frecuencia ~ Respuesta + Realidad,
                                      data = global_freq_dataframe)),
        function(t) t$p.value)))
    svg(paste0(DATA_DIR, "/conf-matrix-global-emotion.svg"))
    plot(plot_conf_matrix(global_freq_dataframe,
                          x_labels = x_labels))
    dev.off()
}

################################################################################
## per-stimulus, group-wide analysis: identify problematic images
################################################################################

main_stimuli <- function() {
    raw_data <- do.call(rbind, lapply(dirs, function(dir) {
        read.csv(paste0(dir, '/subject.csv'), sep = '\t')
    }))
    ## preppend intended emotion to stimulus name, this will help with sorting
    raw_data$stimulus <- paste0(raw_data$emotion, '.',
                                substr(raw_data$stimulus, 28, 999))

    conf_mat <- table(raw_data$response, raw_data$stimulus)

    freq_dataframe <- as.data.frame(conf_mat)
    colnames(freq_dataframe) <- c("Respuesta", "Realidad", "Frecuencia")

    ## group plot
    svg(paste0(DATA_DIR, "/conf-matrix-global-stim.svg"))
    plot(plot_conf_matrix(freq_dataframe,
                          text_size = 3.5,
                          angle = 90,
                          nudge_x = -.3,
                          x_labels_position = "top",
                          x_labels =
                              threshold(unlist(lapply(
                                  multiple_binomial_tests(conf_mat),
                                  function(t) t$p.value)))))
    dev.off()
}

main_emotions()
main_stimuli()
