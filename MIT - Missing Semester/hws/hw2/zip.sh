# find all the files with .html extension
# covert them to html.t
zip_html() {
find *.html | xargs --null tar -cf html.tar
}

