# gha2discord
## Env
```
WEBHOOK_URL="https://discord.com/api/webhooks/[hogehoge]/[hiyohiyo]"
MESSAGE_USERNAME="GitHub Actions"
MESSAGE_AVATAR_URL="https://nyaaaaan.alicey.dev/sugoi_icon.jpg"
MESSAGE_AUTHORNAME="Docker Push"
MESSAGE_AUTHORICON_URL="https://nyaaaaan.alicey.dev/kawaii_icon.jpg"
MESSAGE_COMMENT="なんかpushされたよ\ntagid"
```

## Usage
- GitHubActions yaml (step)
```githubaction.yaml
-
    name: discord notification
    uses: docker://alicey/gha2discord:latest
    env:
        WEBHOOK_URL: ${{ secrets.DC_WEBHOOK_URL }}
        MESSAGE_USERNAME: "GitHub Actions"
        MESSAGE_AVATAR_URL: ""
        MESSAGE_AUTHORNAME: "Docker Push"
        MESSAGE_AUTHORICON_URL: ""
        MESSAGE_COMMENT: "comment\n${{ secrets.DOCKERHUB_USERNAME }}/app-name:${{ env.BUILD_TAG }}"
    with:
        entrypoint: "python3"
        args: "/opt/app/app.py"
```