;; to insert lorem tex type C-x C-l
(defun lorem ()
  "Insert a lorem ipsum."
  (interactive)
  (insert "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do "
          "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim"
          "ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut "
          "aliquip ex ea commodo consequat. Duis aute irure dolor in "
          "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
          "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
          "culpa qui officia deserunt mollit anim id est laborum."))


;; just do C-x C-t to insert the current time
(defun insert-date ()
  "Insert a time-stamp according to locale's date and time format."
  (interactive)
  (insert (format-time-string "%c" (current-time))))

;; go to the end of an expression like (+ 2 2) and type C-x C-u
(defun eval-and-replace ()
  "Replace the preceding sexp with its value."
  (interactive)
  (backward-kill-sexp)
  (condition-case nil
      (prin1 (eval (read (current-kill 0)))
             (current-buffer))
    (error (message "Invalid expression")
           (insert (current-kill 0)))))


(defun current-word ()
  "print current word."
  (interactive)
  (message "%s" (thing-at-point 'word)))

(global-set-key "\C-x\C-w"    'current-word)
(global-set-key "\C-x\C-l"    'lorem)
(global-set-key "\C-x\C-t"    'insert-date)
(global-set-key "\C-x\C-u"    'eval-and-replace)
;; to test eval-and-replace, position the cursor to the end of the following expression
(+ 2 5)

