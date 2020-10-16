## author: Isaac David <isacdaavid@at@isacdaavid@dot@info>
## license: GPLv3 or later

library(gWidgets)
library(gWidgetstcltk)

happy <- read.csv("../emofaces/happy.csv")
happy$gender <- rep("happy", 10)
sad <- read.csv("../emofaces/sad.csv")
sad$gender <- rep("sad", 10)
angry <- read.csv("../emofaces/angry.csv")
angry$gender <- rep("angry", 10)
neutral <- read.csv("../emofaces/neutral.csv")
neutral$gender <- rep("neutral", 10)

stimuli <- rbind(happy, sad, angry, neutral)
names(stimuli) <- c('stimulus', 'emotion')
stimuli$stimulus <- paste0('../emofaces/', stimuli$stimulus)
stimuli$stimulus <- sapply(stimuli$stimulus, function(s) {gsub('tif', 'gif', s)})
stimuli <- stimuli[sample(1:nrow(stimuli)), ]

stimulus_counter <- 1
responses <- c()

win <- gwindow(title = '')
grp <- ggroup(container = win, horizontal = FALSE)
img <- gimage(stimuli[stimulus_counter, 1], container = grp)

handler <- function(selection) {
    responses <<- c(responses, selection)
    if (stimulus_counter <= nrow(stimuli)) {
        stimulus_counter <<- stimulus_counter + 1
        if (stimulus_counter > nrow(stimuli)) {
            dispose(win)
            write.table(cbind(stimuli, response=responses),
                        file = './subject.csv',
                        sep = '\t',
                        row.names = FALSE,
                        fileEncoding = "UTF-8")
            return
        }
        svalue(img) <- stimuli[stimulus_counter, 1]
    }
}

btns <- ggroup(container = grp)

btn_happy <- gbutton(text="Sonriente",
                     container=btns,
                     handler = function(h, ...) {handler('happy')})
btn_happy <- gbutton(text = "Neutra",
                     container = btns,
                     handler = function(h, ...) {handler('neutral')})
btn_happy <- gbutton(text="Triste",
                     container=btns,
                     handler = function(h, ...) {handler('sad')})
btn_happy <- gbutton(text="Enojada",
                     container=btns,
                     handler = function(h, ...) {handler('angry')})

