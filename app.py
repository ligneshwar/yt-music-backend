from flask import Flask, request, jsonify
from yt_dlp import YoutubeDL

app = Flask(__name__)

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "No query provided"}), 400

    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "quiet": True,
            "noplaylist": True,
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch1:{query}", download=False)["entries"][0]
            return jsonify({
                "title": info["title"],
                "url": info["url"],
                "thumbnail": info["thumbnail"]
            })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
