# Git 练习路线

## 练习 1：观察仓库状态

```bash
git status
git log --oneline
```

目标：理解当前分支、工作区、暂存区和提交历史。

## 练习 2：创建自己的分支

```bash
git switch -c feature/your-name-task
```

目标：每个人都在自己的分支上修改，避免直接改 `main`。

## 练习 3：修改文件并提交

```bash
git status
git add .
git commit -m "Add my first task update"
```

目标：理解一次提交应该描述一个清楚的小变化。

## 练习 4：合并分支

```bash
git switch main
git merge feature/your-name-task
```

目标：把分支上的工作合并回主线。

## 练习 5：制造并解决冲突

两位协作者分别修改 `tasks.txt` 的同一行，然后尝试合并。

目标：看到冲突标记，手动保留正确内容，再完成提交。
