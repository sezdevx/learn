(defun buffer/insert-name()
    "Insert the name of the current buffer"
    (interactive)
    (insert (buffer-name (current-buffer))))

(message "%s" (buffer-name (current-buffer)))
(message "%s" (mapcar #'buffer-name (buffer-list)))
(message "%s" (buffer-file-name (current-buffer)))
(insert (buffer-name (current-buffer)))
(message "%s" (buffer-string))
(message "-------------------------------------")
(switch-to-buffer "*Messages*")
(message "%s" (buffer-name (current-buffer)))
(message "%s" (buffer-string))
(switch-to-buffer (other-buffer))
(buffer/insert-name)
(message "%s" (buffer-string))
; to see the whole function documentation, uncomment below
; (message "%s" (describe-function 'replace-regexp))
(message "%s" (apply #'concat '("hello" " world " "!")))
(message "%s" (split-string (getenv "PATH") ":"))
(message "%s" (documentation 'read))
(message "%s" (buffer-local-value 'major-mode (current-buffer)))
(switch-to-buffer (other-buffer))
(append-to-file (point-min) (point-max) "/tmp/afile.txt")
(if (file-exists-p "/tmp/afile.txt")
    (delete-file "/tmp/afile.txt"))
(message "%s" (read-string "prompt > "))
; (read-file-name "Enter a file name: ")
(message "%s" (getenv "PATH"))
(setenv "PATH"   (concat
                        (expand-file-name "~/env/bin/mac") ":"
                        (getenv "PATH")))
(message "-------------------------------------")
(message "%s" (getenv "PATH"))
(message "%s" (shell-command-to-string "uname -a"))
(message "%s" (expand-file-name "~/.emacs"))

(defun read-file (filename)
  (with-temp-buffer
    (insert-file-contents filename)
    (buffer-substring-no-properties (point-min) (point-max))))

(message "%s" (read-file "/etc/hosts"))
(message "System Type: %s" system-type)

(defun read-user-file ()
  "File name reading example"
  (interactive)
  (message "File name is %s" (read-file-name "Enter file name:")))

(defun read-user-dir ()
  "Dir name reading example"
  (interactive)
  (message "Dir name is %s" (read-directory-name "Enter directory name:")))

(defun read-user-str ()
  "String reading example"
  (interactive)
  (message "String is %s" (read-string "Enter string:")))

(if (y-or-n-p "Do it?")
    (message "Done")
  (message "Not Done"))

(defun ask-name (x)
  "Ask name."
  (interactive "sEnter your name: ")
  (message "Name: %s" x))

(defun ask-age(x)
  "Ask age."
  (interactive "sEnter your age: ")
  (message "Age: %d" x))

(defun ask-name-age(x y)
  "Ask name and age."
  (interactive "sEnter you name:
nEnter your age:" )
  (message "Name: %s Age: %d" x y))

(message "%d" (line-beginning-position))
(message "%d" (line-end-position))

;; grabs the current line
(setq currentLine
      (buffer-substring-no-properties
       (line-beginning-position)
       (line-end-position)
       ))

