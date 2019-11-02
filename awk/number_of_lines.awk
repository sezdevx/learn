BEGIN {
    i = 0
}
{ i++ }
END {
    print FILENAME
    # print ARGV[1]
    print i
    # print NR
}
