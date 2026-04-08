// FICHIER COMPLET CORRIGÉ

"use client";
import { useEffect, useState } from "react";
import Link from "next/link";                        // CORRECTION 3 — ajouter
import { getMe, getMySubscription } from "@/lib/api"; // CORRECTION 1 — ajouter

export default function DashboardPage() {
  const [user, setUser] = useState<{name: string; email: string} | null>(null);
  const [sub, setSub] = useState<{plan: string; status: string} | null>(null);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) { window.location.href = "/auth/login"; return; }

    // CORRECTION 1 — remplacer les fetch directs par les fonctions api.ts
    getMe()
      .then(setUser)
      .catch(() => window.location.href = "/auth/login");

    getMySubscription()
      .then(setSub)
      .catch(() => setSub(null));
  }, []);

  if (!user) return (
    <main style={{ minHeight: "100vh", padding: "120px 40px 40px", background: "#0A0908" }}>
      <p style={{ color: "#C8B89A" }}>Loading...</p>
    </main>
  );

  return (
    <main style={{ minHeight: "100vh", padding: "120px 40px 40px", background: "#0A0908", fontFamily: "'Cormorant Garamond', serif" }}>
      <h1 style={{ fontSize: "40px", fontWeight: 300, color: "#F5F0E8", marginBottom: "16px" }}>
        Welcome, {user.name}
      </h1>
      <p style={{ color: "#C8B89A", fontSize: "16px", marginBottom: "8px" }}>Email: {user.email}</p>
      <p style={{ color: "#C8B89A", fontSize: "16px", marginBottom: "32px" }}>
        Plan: {sub ? `${sub.plan} (${sub.status})` : "No active subscription"}
      </p>
      <Link href="/dashboard/rentals" style={{ color: "#D4AF37", fontSize: "14px", letterSpacing: "0.2em", textTransform: "uppercase", textDecoration: "none", borderBottom: "1px solid rgba(212,175,55,0.4)", paddingBottom: "4px" }}>
        My Rentals →
      </Link>
    </main>
  );
}