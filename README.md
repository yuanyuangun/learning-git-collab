# Git 协作练习仓库

这是一个用于学习 Git 版本管理和协同开发的练习仓库。你可以用它练习：

- `clone` / `pull` / `push`
- `branch` / `checkout` / `switch`
- `add` / `commit`
- `merge` / `rebase`
- 解决冲突
- 模拟多人协作流程

## 项目内容

这个仓库包含一个极简任务清单项目：

- `app.py`：命令行任务清单程序
- `tasks.txt`：示例任务数据
- `docs/git-practice.md`：推荐练习路线
- `docs/collaboration-flow.md`：协作者流程说明

## 快速开始

```bash
git clone https://github.com/yuanyuangun/learning-git-collab.git
cd learning-git-collab
python3 app.py
```

如果你已经在本地仓库目录中，也可以直接运行：

```bash
python3 app.py
```

## GitHub 协作练习

真实协作时，可以先邀请协作者：

- 打开仓库 Settings
- 进入 Collaborators
- 输入协作者 GitHub 用户名或邮箱
- 发送邀请

每位协作者 clone 仓库后，从自己的分支开始：

```bash
git clone https://github.com/yuanyuangun/learning-git-collab.git
cd learning-git-collab
git switch -c feature/my-change
```

修改文件并提交后：

```bash
git add .
git commit -m "Practice my change"
git push -u origin feature/my-change
```

然后在 GitHub 上创建 Pull Request，或者本地合并后推送 `main`。

```bash
git switch main
git pull
git merge feature/my-change
git push
```

## 推荐分工

你和协作者可以这样练习：

- A 同学：新增任务筛选功能
- B 同学：修改欢迎文案和帮助信息
- C 同学：补充 README 或文档

每个人从自己的分支开始工作，完成后合并到 `main`。
