import Link from "next/link";
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
export default function ItemCard({ item }: { item: Item }) {
  return (
    <Link href={`/catalog/${item.id}`} style={{ textDecoration: "none" }}>
      <div style={{
        border: "1px solid rgba(212,175,55,0.2)",
        borderRadius: "12px",
        overflow: "hidden",
        background: "#111009",
        opacity: item.available ? 1 : 0.5,
        cursor: item.available ? "pointer" : "not-allowed",
        transition: "box-shadow 0.3s"
      }}>
        <div style={{ width: "100%", height: "280px", overflow: "hidden" }}>
          {item.images && item.images.length > 0 ? (
            <img
              src={item.images[0]}
              alt={item.name}
              style={{ width: "100%", height: "100%", objectFit: "cover" }}
            />
          ) : (
            <div style={{ width: "100%", height: "100%", background: "#1a1a1a" }} />
          )}
        </div>
        <div style={{ padding: "16px" }}>
          <h2 style={{ color: "#F5F0E8", fontFamily: "'Cormorant Garamond', serif", fontSize: "18px", fontWeight: 600, marginBottom: "6px" }}>{item.name}</h2>
          <p style={{ color: "#6B5E4E", fontSize: "13px", marginBottom: "8px" }}>{item.brand} · Size {item.size}</p>
          <p style={{ color: "#D4AF37", fontSize: "16px", fontWeight: 600 }}>{item.price} MAD/month</p>
          <span style={{
            fontSize: "11px", padding: "4px 10px", borderRadius: "20px", marginTop: "8px", display: "inline-block",
            background: item.available ? "rgba(34,197,94,0.1)" : "rgba(107,114,128,0.1)",
            color: item.available ? "#22c55e" : "#6b7280"
          }}>
            {item.available ? "Available" : "Rented"}
          </span>
        </div>
      </div>
    </Link>
  );
}