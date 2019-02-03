(defun hello(name)
    (message "Hello %s" name))

(setq name (read-from-minibuffer "Enter your name: "))
(hello name)
(setq list-of-names '("Me" "You" "Him" "Her"))
(push name list-of-names)
(mapcar 'hello list-of-names)
(hello (car list-of-names))
(mapcar 'hello (cdr list-of-names))

