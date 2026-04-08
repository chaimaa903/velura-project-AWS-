"use client";
import { useEffect, useState } from "react";
import { getItem, rentItem } from "@/lib/api";
import Link from "next/link";

export default function ItemDetailPage({ params }: { params: { id: string } }) {
  const [item, setItem] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [rented, setRented] = useState(false);

  useEffect(() => {
    getItem(Number(params.id))
      .then(setItem)
      .catch(console.error);
  }, [params.id]);

  const handleRent = async () => {
    const token = localStorage.getItem("token");
    if (!token) { window.location.href = "/auth/login"; return; }
    try {
      setLoading(true);
      await rentItem(item.id);
      setRented(true);
      setItem((prev: any) => ({ ...prev, available: false }));
    } catch {
      alert("Failed to rent item");
    } finally {
      setLoading(false);
    }
  };

  if (!item) return (
    <main style={{ minHeight: "100vh", padding: "120px 40px 40px", background: "#0A0908" }}>
      <p style={{ color: "#C8B89A", fontFamily: "'Cormorant Garamond', serif" }}>Loading...</p>
    </main>
  );

  return (
    <main style={{
      minHeight: "100vh", padding: "120px 40px 40px",
      background: "#0A0908", fontFamily: "'Cormorant Garamond', serif",
    }}>

      {/* Breadcrumb */}
      <Link href="/catalog" style={{
        fontSize: "12px", letterSpacing: "0.2em", color: "#6B5E4E",
        textDecoration: "none", textTransform: "uppercase",
        display: "inline-block", marginBottom: "40px",
      }}>
        ← Back to Collection
      </Link>

      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "80px", alignItems: "start" }}>

        {/* Image */}
        <div>
          {item.images && item.images.length > 0 ? (
            <img
              src={item.images[0]}
              alt={item.name}
              style={{ width: "100%", height: "600px", objectFit: "cover" }}
            />
          ) : (
            <div style={{
              width: "100%", height: "600px",
              background: "#1A1714",
              display: "flex", alignItems: "center", justifyContent: "center",
            }}>
              <span style={{ color: "#3D3328", fontSize: "14px", letterSpacing: "0.2em" }}>NO IMAGE</span>
            </div>
          )}
        </div>

        {/* Infos */}
        <div>
          <p style={{ fontSize: "11px", letterSpacing: "0.3em", color: "#D4AF37", textTransform: "uppercase", marginBottom: "16px" }}>
            {item.category} · Size {item.size}
          </p>

          <h1 style={{ fontSize: "48px", fontWeight: 300, color: "#F5F0E8", lineHeight: 1.1, marginBottom: "8px" }}>
            {item.name}
          </h1>

          <p style={{ fontSize: "18px", color: "#6B5E4E", marginBottom: "32px", letterSpacing: "0.1em" }}>
            {item.brand}
          </p>

          <p style={{ fontSize: "36px", fontWeight: 300, color: "#D4AF37", marginBottom: "48px" }}>
            {item.price} <span style={{ fontSize: "14px", color: "#6B5E4E" }}>MAD/month</span>
          </p>

          {/* Badge disponibilité */}
          <div style={{ marginBottom: "32px" }}>
            <span style={{
              fontSize: "11px", letterSpacing: "0.2em", textTransform: "uppercase",
              padding: "6px 16px",
              background: item.available ? "rgba(212,175,55,0.1)" : "rgba(255,255,255,0.05)",
              color: item.available ? "#D4AF37" : "#4A3F35",
              border: `1px solid ${item.available ? "rgba(212,175,55,0.3)" : "rgba(255,255,255,0.05)"}`,
            }}>
              {item.available ? "Available" : "Currently Rented"}
            </span>
          </div>

          {/* Message succès */}
          {rented && (
            <p style={{ color: "#D4AF37", fontSize: "14px", letterSpacing: "0.1em", marginBottom: "24px" }}>
              ✓ Item rented successfully! Check your rentals.
            </p>
          )}

          {/* Bouton Rent */}
          <button
            onClick={handleRent}
            disabled={!item.available || loading || rented}
            style={{
              width: "100%", padding: "18px",
              background: item.available && !rented ? "#D4AF37" : "#1A1714",
              border: item.available && !rented ? "none" : "1px solid rgba(212,175,55,0.15)",
              color: item.available && !rented ? "#0A0908" : "#3D3328",
              fontSize: "12px", letterSpacing: "0.3em",
              textTransform: "uppercase", fontWeight: 700,
              fontFamily: "'Cormorant Garamond', serif",
              cursor: item.available && !rented ? "pointer" : "not-allowed",
            }}
          >
            {rented ? "Rented ✓" : loading ? "Processing..." : item.available ? "Rent Now" : "Unavailable"}
          </button>

          {/* Lien rentals */}
          {rented && (
            <Link href="/dashboard/rentals" style={{
              display: "block", textAlign: "center", marginTop: "16px",
              fontSize: "12px", letterSpacing: "0.2em", color: "#D4AF37",
              textTransform: "uppercase", textDecoration: "none",
            }}>
              View My Rentals →
            </Link>
          )}
        </div>
      </div>
    </main>
  );
}