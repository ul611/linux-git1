# !usr/local/bin/bash

nickname=$1

PULLS=0

for i in `seq 4`
do

PULLS=$((PULLS+$(curl -s -H "Accept: application/vnd.github.v3+json" 'https://api.github.com/repos/datamove/linux-git2/pulls?state=all&per_page=100&page='"$i" | jq '.[].user.login' | grep "$nickname" | wc -l)))
done

echo 'PULLS '"$PULLS"

EARLIEST=0
FLAG=0

for i in 4 3 2 1
do

TMP=$(curl -s -H "Accept: application/vnd.github.v3+json" 'https://api.github.com/repos/datamove/linux-git2/pulls?state=all&per_page=100&page='"$i" | jq 'map(select(.user.login=="'"$nickname"'"))' | jq '.[].number' | tail -1)
EARLIEST=$(( FLAG==1 ? EARLIEST : (TMP ? TMP : EARLIEST) ))
FLAG=$(( TMP ? 1 : FLAG ))

done


MERGED=$(curl -s -H "Accept: application/vnd.github.v3+json" 'https://api.github.com/repos/datamove/linux-git2/pulls/'"$EARLIEST" | jq '.merged')
echo 'EARLIEST '"$EARLIEST"

if ["$MERGED" = "true"] ; then MERGED=1 ; else MERGED=0 ; fi

echo 'MERGED '"$MERGED"
