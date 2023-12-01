

git rev-list --count HEAD

git rebase -i main~400 -x "git commit --amend --author 'MariuszKolodziejLX <mariuszkolodziej@luxmed.pl>' --no-edit --force"

git pull origin main --allow-unrelated-histories


git rebase -i main~400 -x "git commit --amend --author 'MariuszKolodziejLX <mariuszkolodziej@luxmed.pl>' --no-edit" --strategy=ours --autostash --allow-empty



git rebase -i main~400 -x "git commit --amend --author='MariuszKolodziejLX <mariuszkolodziej@luxmed.pl>' --no-edit" --strategy=theirs  --autostash --allow-empty



git commit --allow-empty


git rebase --skip