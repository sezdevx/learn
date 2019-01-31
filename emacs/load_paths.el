(defun printLoadPath(name)
    (message "Load Path: %s" name)
)

(mapcar 'printLoadPath load-path)
