"use client";
import { useState } from "react";
import { chatWithStylist } from "@/lib/api";

export default function AIStylistPage() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState<{ role: string; content: string }[]>([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!message.trim()) return;
    const currentMessage = message;
    setChat(prev => [...prev, { role: "user", content: currentMessage }]);
    setMessage("");
    setLoading(true);
    try {
      const data = await chatWithStylist(currentMessage, chat);
      setChat(prev => [...prev, { role: "assistant", content: data.response }]);
    } catch {
      setChat(prev => [...prev, { role: "assistant", content: "Error connecting to AI." }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ minHeight: "100vh", background: "#0A0908", padding: "120px 40px 40px", fontFamily: "'Cormorant Garamond', serif" }}>
      <div style={{ maxWidth: "700px", margin: "0 auto" }}>

        <h1 style={{ fontSize: "40px", fontWeight: 300, color: "#F5F0E8", marginBottom: "8px" }}>
          AI Stylist
        </h1>
        <p style={{ color: "#6B5E4E", marginBottom: "32px", fontSize: "14px", letterSpacing: "0.1em" }}>
          Ask me anything about fashion...
        </p>

        <div style={{ border: "1px solid rgba(212,175,55,0.15)", padding: "24px", height: "400px", overflowY: "auto", marginBottom: "24px", display: "flex", flexDirection: "column", gap: "16px", background: "#0F0D0B" }}>
          {chat.length === 0 && (
            <p style={{ color: "#3D3328", fontSize: "14px" }}>
              Start a conversation with your personal stylist...
            </p>
          )}
          {chat.map((m, i) => (
            <div key={i} style={{ display: "flex", justifyContent: m.role === "user" ? "flex-end" : "flex-start" }}>
              <div style={{ maxWidth: "80%", padding: "12px 16px", background: m.role === "user" ? "#D4AF37" : "rgba(212,175,55,0.08)", color: m.role === "user" ? "#0A0908" : "#C8B89A", fontSize: "15px", lineHeight: 1.6 }}>
                {m.content}
              </div>
            </div>
          ))}
          {loading && (
            <p style={{ color: "#4A3F35", fontSize: "13px", fontStyle: "italic" }}>
              Velura AI is thinking...
            </p>
          )}
        </div>

        <div style={{ display: "flex", gap: "12px" }}>
          <input
            value={message}
            onChange={e => setMessage(e.target.value)}
            onKeyDown={e => e.key === "Enter" && sendMessage()}
            placeholder="Ask your stylist..."
            style={{ flex: 1, padding: "16px", background: "transparent", border: "1px solid rgba(212,175,55,0.3)", color: "#F5F0E8", fontSize: "15px", fontFamily: "'Cormorant Garamond', serif", outline: "none" }}
          />
          <button
            onClick={sendMessage}
            disabled={loading}
            style={{ padding: "16px 32px", background: "#D4AF37", border: "none", color: "#0A0908", fontSize: "12px", letterSpacing: "0.25em", textTransform: "uppercase", fontWeight: 700, cursor: loading ? "wait" : "pointer" }}>
            {loading ? "..." : "Send"}
          </button>
        </div>

      </div>
    </div>
  );
}