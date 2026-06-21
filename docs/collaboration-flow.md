# 协同开发流程

推荐使用这个节奏：

1. 从 `main` 更新最新代码。
2. 创建自己的功能分支。
3. 在分支上完成小步提交。
4. 合并前再次同步 `main`。
5. 解决冲突并测试。
6. 合并回 `main`。

常用命令：

```bash
git switch main
git pull
git switch -c feature/name
git add .
git commit -m "Describe the change"
git switch main
git merge feature/name
```

如果这个仓库还没有远程地址，可以先在 GitHub、GitLab 或 Gitee 上创建一个空仓库，然后添加远程：

```bash
git remote add origin <远程仓库地址>
git push -u origin main
```
