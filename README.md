# leetcode

## レビュー用 PR の作り方

GitHub の **Issues → New issue → LeetCode のレビュー依頼を作成** を開き、次の項目を入力します。

1. LeetCode の問題 URL
2. 言語（Python または C++）
3. step 1、step 2、step 3 のコード

Issue を作成すると、GitHub Actions が次のものを自動作成します。

- `question/<問題名>-<Issue番号>` ブランチ
- `<問題名>/step1.py`、`step2.py`、`step3.py`（C++ の場合は `.cpp`）
- `main` 向けのレビュー用 Pull Request

同じ問題のディレクトリがすでにある場合は、`(retry)` を付けて別ディレクトリに保存します。PR がマージされると、入力に使った Issue も自動で閉じます。

### 初回のみ必要な設定

リポジトリの **Settings → Actions → General → Workflow permissions** で次を設定してください。

- **Read and write permissions** を選択する
- **Allow GitHub Actions to create and approve pull requests** を有効にする

自動作成を実行できるのは、このリポジトリへの書き込み権限を持つユーザーだけです。
