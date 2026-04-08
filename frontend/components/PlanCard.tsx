"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import { subscribe } from "@/lib/api";

interface PlanCardProps {
  name: string;
  price: number;
  description: string;
  features: string[];
  isPopular?: boolean;
}

export default function PlanCard({ name, price, description, features, isPopular = false }: PlanCardProps) {
  const router = useRouter();
  const [loading, setLoading] = useState(false);

  const handleChoosePlan = async () => {
    const token = localStorage.getItem("token");
    if (!token) {
      router.push("/auth/register");
      return;
    }
    try {
      setLoading(true);
      await subscribe(name);
      router.push("/dashboard");
    } catch (err) {
      console.error("Subscribe failed:", err);
    } finally {
      setLoading(false);
    }
  };

  return (                                            // ← AJOUTER return (
    <div style={{
      position: "relative",
      background: "#0F0D0B",
      border: isPopular ? "1px solid rgba(212,175,55,0.5)" : "1px solid rgba(212,175,55,0.12)",
      padding: "48px 40px",
      fontFamily: "'Cormorant Garamond', serif",
      transform: isPopular ? "scale(1.03)" : "scale(1)",
    }}>
      {isPopular && (
        <div style={{
          position: "absolute", top: "-1px", left: "40px",
          background: "#D4AF37", color: "#0A0908",
          fontSize: "10px", letterSpacing: "0.25em",
          textTransform: "uppercase", fontWeight: 700, padding: "5px 16px",
        }}>Most Popular</div>
      )}

      <h3 style={{
        fontSize: "13px", letterSpacing: "0.3em", color: "#D4AF37",
        textTransform: "uppercase", fontWeight: 600,
        marginBottom: "24px", marginTop: isPopular ? "12px" : "0",
      }}>{name}</h3>

      <div style={{ display: "flex", alignItems: "baseline", gap: "4px", marginBottom: "16px" }}>
        <span style={{ fontSize: "52px", fontWeight: 300, color: "#F5F0E8", lineHeight: 1 }}>
          {price}
        </span>
        <span style={{ fontSize: "14px", color: "#6B5E4E" }}>MAD/month</span>
      </div>

      <p style={{
        fontSize: "14px", color: "#6B5E4E", lineHeight: 1.7, marginBottom: "36px",
        paddingBottom: "36px", borderBottom: "1px solid rgba(212,175,55,0.1)",
      }}>{description}</p>

      <ul style={{ listStyle: "none", padding: 0, margin: "0 0 40px 0" }}>
        {features.map((f) => (
          <li key={f} style={{
            display: "flex", alignItems: "center", gap: "12px",
            color: "#C8B89A", fontSize: "14px", marginBottom: "14px",
          }}>
            <span style={{ color: "#D4AF37" }}>—</span>{f}
          </li>
        ))}
      </ul>

      <button
        onClick={handleChoosePlan}
        disabled={loading}
        style={{
          display: "block", width: "100%", textAlign: "center",
          fontFamily: "'Cormorant Garamond', serif",
          fontSize: "12px", letterSpacing: "0.25em",
          textTransform: "uppercase", fontWeight: 700,
          cursor: loading ? "wait" : "pointer",
          padding: "14px 32px",
          background: isPopular ? "#D4AF37" : "transparent",
          color: isPopular ? "#0A0908" : "#D4AF37",
          border: isPopular ? "none" : "1px solid rgba(212,175,55,0.35)",
        }}>
        {loading ? "Processing..." : "Choose Plan"}
      </button>

    </div>
  );               // ← fermer le return
}