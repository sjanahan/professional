In order to prevent unnecessary MERGE commits to master, follow this procedure
```
(---) git checkout mori
(mori) git rebase master
(mori) git push origin --force
*make PR, it gets approved*
(mori) git checkout master
(master) git rebase mori
(master) git push origin
```

