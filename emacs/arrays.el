(defun hello(name) (message "Hello %s" name))

(message "Is array? %s" (arrayp nil))
(message "Is array? %s" (arrayp [0]))
(message "Is array? %s" (arrayp "abcd"))
(message "Array elem = %s" (aref "abcd" 0))
(message "Array elem = %s" (aref "abcd" 1))
(message "Array elem = %d" (aref [0 11 22 33 44] 2))
(setq a [0 1 2 3 4])
(message "%s" a)
(fillarray a 0)
(message "%s" a)
(setq s "abcdefghijklmno")
(message "%s" s)
(fillarray s ?-)
(message "%s" s)
(fillarray s ?x)
(message "%s" s)
(setq v [1 two '(three) "four" [five]])
(message "%s" v)
(message "Is Vector? %s" (vectorp v))
(message "%s" (make-vector 9 'z))
