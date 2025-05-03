from utils.transcript import get_transcript, extract_video_id
from utils.chunking import chunk_text
from utils.embed_store import embed_chunks
from utils.query import get_qa_chain, ask_question

def main():
    url = input("🔗 Enter YouTube video URL: ")
    video_id = extract_video_id(url)
    if not video_id:
        print("❌ Invalid URL.")
        return

    print("⏳ Fetching transcript...")
    transcript = get_transcript(video_id)

    print("✂️ Chunking transcript...")
    chunks = chunk_text(transcript)

    print("🔗 Embedding and storing chunks...")
    vectorstore = embed_chunks(chunks)

    print("✅ Ready. Ask questions about the video (type 'exit' to quit):")
    chain = get_qa_chain(vectorstore)
    
    while True:
        query = input("\n❓ Your question: ")
        if query.lower() == "exit":
            break
        answer = ask_question(chain, query)
        print(f"\n💬 Answer: {answer}")

if __name__ == "__main__":
    main()