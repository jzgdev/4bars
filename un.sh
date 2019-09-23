project=Piotrek173-ClyphxSessions.als
cp "/Users/piotrek/LiveWorkspace/Piotrek 102 Kombi Project/$project" "un/$project"
cd un && gzip -cd $project > $project.xml
