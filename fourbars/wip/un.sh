project=bazille-spire.als
cp "/Users/piotrek/.config/4bars/bazille-spire Project/$project" "un/$project"
cd un && gzip -cd $project > $project.xml
