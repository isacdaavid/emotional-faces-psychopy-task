
## author: Isaac David <isacdaavid@at@isacdaavid@dot@info>
## license: GPLv3 or later

library(lme4)
library(nlme)
library(ggplot2)
BASE_SIZE <- 21
theme_set(theme_gray(base_size = BASE_SIZE))

DATA_DIR <- './emofaces/data/'
files <- list.files(DATA_DIR, "*.csv")
files <- files[11:length(files)] # exclude Pablo (missing data) and myself

## load single Psychopy CSV output and make sense of its messiness. very hacky
##
## input: path to file
## output: clean dataframe
parse_file <- function(path) {
    data <- read.csv(path)
    ## only the following columns contain useful info
    data <- data[, c("stimulus",
                     "gender",
                     "key_resp_2.keys",
                     "key_resp_3.keys",
                     "key_resp_4.keys",
                     "key_resp_5.keys",
                     "key_resp_6.keys",
                     "key_resp_7.keys",
                     "key_resp_2.rt",
                     "key_resp_3.rt",
                     "key_resp_4.rt",
                     "key_resp_5.rt",
                     "key_resp_6.rt",
                     "key_resp_7.rt")]
    data[is.na(data)] <- 0              # so as to sum RT's with NA's
    data <- data.frame(stimulus = unname(data["stimulus"]),
                       gender = data$gender,
                       keys = trimws(paste(data$key_resp_2.keys,
                                           data$key_resp_3.keys,
                                           data$key_resp_4.keys,
                                           data$key_resp_5.keys,
                                           data$key_resp_6.keys,
                                           data$key_resp_7.keys)),
                       rt = Reduce("+", data[, 9:14]))
    data$rt[data$rt == 0] <- NA         # RT == 0 was actually a NA, after all
    ## map from button keys to implied stimulus gender (m-ale or f-emale)
    data$keys <- sapply(data$keys, function(k) {
        if (k == "b" || k == "a") {"m"}
        else if (k == "c" || k == "d") {"f"}
        else {""}
    })
    ## evaluate responses during non-gendered trials (copy response
    ## key to gender if correct. i.e., if any response was given)
    correct_nongendered <- (data$gender == "") & (! is.na(data$rt))
    data$gender[correct_nongendered] <- data$keys[correct_nongendered]
    ## explicitly make missing responses different from expected gender
    data$keys[is.na(data$rt) & (data$keys == "")] <- "None"
    return(data)
}

## put per-file dataframes (as returned by `parse_file()`) together,
## add extra useful columns
##
## input: filenames vector
## output: global dataframe
parse_files <- function(paths) {
    ## row-bind individual dataframes
    dframe <- do.call(rbind, lapply(files, function(path) {
        dframe <- parse_file(paste0(DATA_DIR, path))
        run <- regexpr("emofaces", path) + 8 # parse experiment number (1-5)
        sub_id <- substr(path, 1, 2)         # parse subject id
        cbind(subject = rep(sub_id, nrow(dframe)),
              run = rep(as.numeric(substring(path, run, run)), nrow(dframe)),
              dframe,
              ## whether gender matches key response (abstract away
              ## actual gender)
              respuesta = (dframe$gender == dframe$keys))
    }))
    ## add trial count for each subject. this is easier once all 5
    ## runs per subject reside in one dataframe
    dframe <-
        cbind(dframe,
              ensayo = do.call(c, lapply(unique(dframe$subject), function(s) {
                  1:nrow(dframe[dframe$subject == s, ])
              })),
              bloque = do.call(c, lapply(unique(dframe$subject), function(s) {
                  c(rep("blank", 10),
                    rep("scrambled", 10),
                    rep("happy", 10),
                    rep("sad", 10),
                    rep("angry", 10),
                    rep("neutral", 10),
                    rep("happy", 10),
                    rep("sad", 10),
                    rep("angry", 10),
                    rep("neutral", 10),
                    rep("scrambled", 10),
                    rep("blank", 10),
                    ## run 2
                    rep("sad", 10),
                    rep("neutral", 10),
                    rep("blank", 10),
                    rep("angry", 10),
                    rep("scrambled", 10),
                    rep("happy", 10),
                    rep("sad", 10),
                    rep("neutral", 10),
                    rep("blank", 10),
                    rep("angry", 10),
                    rep("scrambled", 10),
                    rep("happy", 10),
                    ## run 3
                    rep("neutral", 10),
                    rep("blank", 10),
                    rep("angry", 10),
                    rep("scrambled", 10),
                    rep("happy", 10),
                    rep("sad", 10),
                    rep("neutral", 10),
                    rep("blank", 10),
                    rep("angry", 10),
                    rep("scrambled", 10),
                    rep("happy", 10),
                    rep("sad", 10),
                    ## run 4
                    rep("happy", 10),
                    rep("angry", 10),
                    rep("neutral", 10),
                    rep("blank", 10),
                    rep("sad", 10),
                    rep("scrambled", 10),
                    rep("happy", 10),
                    rep("angry", 10),
                    rep("neutral", 10),
                    rep("blank", 10),
                    rep("sad", 10),
                    rep("scrambled", 10),
                    ## run 5
                    rep("scrambled", 10),
                    rep("sad", 10),
                    rep("happy",10),
                    rep("neutral", 10),
                    rep("angry", 10),
                    rep("blank", 10),
                    rep("scrambled", 10),
                    rep("sad", 10),
                    rep("happy", 10),
                    rep("neutral", 10),
                    rep("angry", 10),
                    rep("blank", 10))
              })))
    dframe$bloque <- factor(dframe$bloque,
                            levels = c("blank", "scrambled", "neutral", "happy",
                                       "sad", "angry"))
    return(dframe)
}

df <- parse_files(files)

################################################################################
## hits vs misses
################################################################################

## reduced dataframe with hits and misses count per trial,
## irrespective of subject
df2 <- do.call(rbind, lapply(unique(df$ensayo), function(t) {
    data.frame(ensayo = c(t, t),
               respuesta = factor(c("errores", "aciertos"),
                                  c("errores", "aciertos")),
               sujetos = c(nrow(df[df$ensayo == t & df$respuesta == FALSE, ]),
                       nrow(df[df$ensayo == t & df$respuesta == TRUE, ])))
}))

## perform per-subject binomial tests
pvals <- unname(sapply(unique(df$subject), function(s) {
    binom.test(table(df[df$subject == s, "respuesta"])["TRUE"],
               n = length(df[df$subject == s, "respuesta"]),
               p = 1/2,
               alternative = "greater")$p.value
}))
pvals <- p.adjust(pvals, method="holm") # Holm's FWE p-value correction

## perform per-block-type binomial tests
pvals_block <- unname(sapply(unique(df$bloque), function(b) {
    binom.test(table(df[df$bloque == b, "respuesta"])["TRUE"],
               n = length(df[df$bloque == b, "respuesta"]),
               p = 1/2,
               alternative = "greater")$p.value
}))
pvals_block<- p.adjust(pvals_block, method="holm") # Holm's FWE p-value correction

## plot group performance timeseries as proportion between hits and misses
svg("./cumm-hits-vs-misses-timeseries.svg", width=10, height=4.5)
ggplot(df2, aes(x = ensayo, y = sujetos, fill = respuesta)) +
    geom_area() +
    scale_x_continuous(breaks = seq(0, 600, 10),
                       labels = sapply(seq(0, 600, 10), function(l) {
                           if (l %% 120 == 0) l else ""
                       })) +
    ## scale_y_continuous(breaks = seq(0, 12, 2), labels = seq(0, 12, 2)) +
    theme(axis.text.x = element_text(angle = 90, hjust = 1, vjust = .5),
          legend.position = "bottom") +
    labs(caption = paste("Prueba binomial del peor sujeto: valor p (Holm) =",
                         signif(max(pvals), 3),
                         "\nPrueba binomial del peor tipo de bloque: valor p (Holm) = ",
                         signif(max(pvals_block), 3)))
dev.off()

################################################################################
## reaction times
################################################################################

## linear
modelo <- lm(rt ~ ensayo + bloque, data = df)
summary(modelo)
par(mfrow = c(2,2))
plot(modelo)

## general linear. same results but provides benchmark to compare with lme
modelo_glm <- gls(rt ~ ensayo + bloque, data = df,  method = "ML", na.action = na.omit)
summary(modelo_glm)
svg("rt-timeseries-model-selection-res1.svg")
plot.new()
plot(modelo_glm)
abline(.3, 0)
dev.off()

## now we add mixed effects
modelo_glmm <- lme(rt ~ run + bloque,
                   random = ~1|subject, data = df,
                   method = "ML",
                   na.action = na.omit)
summary(modelo_glmm)
svg("rt-random-effects.svg")
plot(ranef(modelo_glmm))                # random effects
dev.off()
svg("rt-timeseries-model-selection-res2.svg")
plot.new()
plot(modelo_glmm)
dev.off()

## model-selection criteria
comp <- anova(modelo_glm, modelo_glmm)

## plot model comparison diagnostics. very hacky!
svg("./rt-timeseries-model-selection.svg")
par(mfrow = c(2,2))
qqnorm(resid(modelo_glm, type = "normalized"), main = "Modelo efectos fijos")
qqline(resid(modelo_glm, type = "normalized"))
qqnorm(resid(modelo_glmm, type = "normalized"), main = "Modelo efectos mixtos")
qqline(resid(modelo_glmm, type = "normalized"))
title(paste0("\nComparación de modelos de regresión\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",
             "                        AIC: ",
             as.integer(comp$AIC[1]),
             "                                                                              ",
             as.integer(comp$AIC[2]),
             "\n                        BIC: ",
             as.integer(comp$BIC[1]),
             "                                                                              ",
             as.integer(comp$BIC[2]),
             "\nlog-verosimilitud: ",
             as.integer(comp$logLik[1]),
             "                                                                             ",
             as.integer(comp$logLik[2])),
      outer=TRUE)
dev.off()

## plot reaction time timeseries (with fits)
svg("./rt-timeseries-fit.svg", width = 10, height = 5)
ggplot(df, aes(x = ensayo, y = rt, group = subject, color = subject)) +
    geom_smooth(show.legend = FALSE, method = "loess", span = .1, alpha = .3) +
    ## geom_abline(aes(intercept = modelo$coefficients[1],
    ##                 slope = modelo$coefficients[2],
    ##                 color = "red"), show.legend = FALSE) +
    geom_abline(aes(intercept = modelo_glmm$coefficients$fixed[1],
                    slope = modelo_glmm$coefficients$fixed[2] / 120),
                show.legend = FALSE, linetype = "dashed") +
    ## scale_y_continuous(limits = c(0, 3)) +
    scale_x_continuous(breaks = seq(0, 600, 10),
                       labels = sapply(seq(0, 600, 10), function(l) {
                           if (l %% 120 == 0) l else ""
                       })) +
    theme(axis.text.x = element_text(angle = 90, hjust = 1, vjust = .5)) +
    labs(y = "tiempo de reacción (s)",
         caption = paste0("\ntiempo = ",
                          signif(modelo_glmm$coefficients$fixed[2]/120, 2),
                          " \u00B7 ensayo  + X \u00B7 bloque + U \u00B7 sujeto  +  ",
                          signif(modelo_glmm$coefficients$fixed[1], 2),
                          "\nValores p : ",
                          signif(summary(modelo_glmm)$tTable[2,5], 3),
                          ",                                                  ",
                          signif(summary(modelo_glmm)$tTable[1,5], 3)))
dev.off()

## block-type anova
anova <- aov(rt ~ bloque, data = df)
summary(anova)
TukeyHSD(anova)
