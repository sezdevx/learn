(defun hello(name) (message "Hello %s" name))
(defun printNumber(num) (message "%d" num))


(setq names '("Me" "You"))
(mapcar 'hello names)
(message "Added Him to the beginning of the list")
(add-to-list 'names "Him")
(mapcar 'hello names)
(add-to-list 'names "Her" t)
(message "Added Her to the end of the list")
(mapcar (quote hello) names)
(setq names (delete "Her" names))
(message "Removed Her from the list")
(mapcar (quote hello) names)
(message "Added Her to the beginning of the list")
(setq names (cons "Her" names))
(mapcar (quote hello) names)
(message "First in the list is %s" (car names))
(message "The rest of the list is")
(mapcar (quote hello) (cdr names))

(message "Is consp %s" (consp names))
(message "Is consp %s" (consp nil))
(message "Is atom %s" (atom names))
(message "Is atom %s" (atom nil))
(message "Is atom %s" (atom t))
(message "Is atom %s" (atom 12))
(message "Is listp %s" (listp nil))
(message "Is listp %s" (listp names))
(message "Is listp %s" (listp 12))
(message "Is listp %s" (listp t))
(message "Is nlistp %s" (nlistp nil))
(message "Is nlistp %s" (nlistp names))
(message "Is nlistp %s" (nlistp 12))
(message "Is nlistp %s" (nlistp t))
(message "Is null %s" (null nil))
(message "Is null %s" (null t))

(message "First item %s" (car names))
(message "Second item %s" (car (cdr names)))
(message "List length %d" (safe-length names))

(setq numbers (list 1 2 3 4 5))
(mapcar 'printNumber numbers)
(setq nums2 (make-list 9 9))
(mapcar 'printNumber nums2)
(mapcar 'printNumber (number-sequence 1 5))
(setq l '(a b))
(push 'c l)
(mapcar 'hello l)

(message "Is b member ? %s " (memq 'b l))
(message "Is d member ? %s " (memq 'd l))

(message "Is b member ? %s " (memq 1.2 '(1.2 1.1 1.0)))
(message "Is b member ? %s " (memql 1.2 '(1.2 1.1 1.0)))
(message "Is b member ? %s " (member 1.2 '(1.2 1.1 1.0)))

(setq people '((john . 23) (jane . 40) (ali . 20)))
(mapcar 'hello people)
(hello people)
(hello (cdr (assoc 'john people)))
(hello (cdr (assoc 'jane people)))
(hello (cdr (assoc 'ali people)))
(hello (car (rassoc 40 people)))
(hello (car (rassoc 23 people)))
(hello (car (rassoc 20 people)))
(hello (car (rassoc 30 people)))
