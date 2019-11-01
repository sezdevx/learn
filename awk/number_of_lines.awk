BEGIN {
    i = 0
}
{ i++ }
END {
    print FILENAME
    print i
    # print NR
}
