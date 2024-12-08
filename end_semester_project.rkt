#lang racket
(require data-science-master)
(require plot)
(require math)

;;; Step 1: Load the .csv file
(define csv-data (read-csv "C:/Users/Ethan_Xian/Downloads/uganda_tweets.csv")) ; Replace with your .csv file path

;;; Step 2: Process the data
;;; Extract columns of interest. Assume the .csv file has headers and one of the
;;; columns contains textual data for sentiment analysis.
(define headers (first csv-data))
(define rows (rest csv-data))

;;; Let's assume the text column is named "text"
(define text-col-index (index-of headers "text"))
(define text-data (map (λ (row) (list-ref row text-col-index)) rows))

;;; Normalize, remove punctuation, and tokenize the text
(define processed-texts
  (map (λ (text)
         (document->tokens 
          (string-normalize-spaces
           (remove-punctuation
            (string-downcase text) #:websafe? #t))
          #:sort? #t))
       text-data))

;;; Flatten tokens from all rows into a single list for sentiment analysis
(define all-tokens (apply append processed-texts))

;;; Step 3: Perform sentiment analysis
;;; Using the `list->sentiment` abstraction from `data-science`
(define sentiment (list->sentiment all-tokens #:lexicon 'nrc))

(take sentiment 5)
;;; Step 4: Aggregate sentiment frequencies
(define sentiment-frequencies 
  (aggregate sum ($ sentiment 'sentiment) ($ sentiment 'freq)))

;;; Step 5: Visualize sentiment distribution
(parameterize ((plot-width 800))
  (plot (list
         (tick-grid)
         (discrete-histogram
          (sort sentiment-frequencies (λ (x y) (> (second x) (second y))))
          #:color "MediumSlateBlue"
          #:line-color "MediumSlateBlue"))
        #:x-label "Affective Label"
        #:y-label "Frequency"))
