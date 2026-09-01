# leetcode

## レビュー用 PR の作り方

GitHub の **Issues → New issue → LeetCode のレビュー依頼を作成** を開き、次の項目を入力します。

1. LeetCode の問題 URL
2. 言語（Python、Ruby、C++）
3. step 1、step 2、step 3 のコード
4. 解法、計算量、疑問点などの解説文（Markdown）

Issue を作成すると、GitHub Actions が次のものを自動作成します。

- `question/<問題名>-<Issue番号>` ブランチ
- `<問題名>/step1.<拡張子>`、`step2.<拡張子>`、`step3.<拡張子>`
- 解説文を保存した `<問題名>/memo.md`
- `main` 向けのレビュー用 Pull Request

同じ問題のディレクトリがすでにある場合は、`(retry)` を付けて別ディレクトリに保存します。PR がマージされると、入力に使った Issue も自動で閉じます。

### 初回のみ必要な設定

リポジトリの **Settings → Actions → General → Workflow permissions** で次を設定してください。

- **Read and write permissions** を選択する
- **Allow GitHub Actions to create and approve pull requests** を有効にする

自動作成を実行できるのは、このリポジトリへの書き込み権限を持つユーザーだけです。

### 対応言語を増やす場合

Issue フォームの `Language` の選択肢と、ワークフローの `supportedLanguages` に言語名と拡張子を追加してください。ブランチ・ファイル・PR作成部分を変更する必要はありません。
