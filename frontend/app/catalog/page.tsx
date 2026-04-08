// FICHIER COMPLET CORRIGÉ
"use client";
import { useEffect, useState } from "react";
import ItemCard from "@/components/ItemCard";
import { getItems } from "@/lib/api";

type Item = {
  id: number;
  name: string;
  brand: string;
  category: string;
  size: string;
  price: number;
  images: string[] | null;
  available: boolean;
};

export default function CatalogPage() {
  const [items, setItems] = useState<Item[]>([]);
  const [error, setError] = useState(false);

  useEffect(() => {
    getItems()
      .then(setItems)
      .catch(() => setError(true));
  }, []);

  if (error) return (
    <main style={{ minHeight: "100vh", paddingTop: "120px", padding: "120px 40px 40px", background: "#0A0908" }}>
      <p style={{ color: "#C8B89A" }}>Failed to load items.</p>
    </main>
  );

  return (
    <main style={{ minHeight: "100vh", paddingTop: "120px", padding: "120px 40px 40px", background: "#0A0908" }}>
      <h1 style={{ fontSize: "32px", fontWeight: 300, color: "#F5F0E8", marginBottom: "40px", fontFamily: "'Cormorant Garamond', serif" }}>
        Browse Collection
      </h1>
      <div style={{
        display: "grid",
        gridTemplateColumns: "repeat(auto-fill, minmax(280px, 1fr))",
        gap: "24px",
      }}>
        {items.map((item) => <ItemCard key={item.id} item={item} />)}
      </div>
    </main>
  );
}