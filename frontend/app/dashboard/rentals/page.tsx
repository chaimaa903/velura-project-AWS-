"use client";
import { useEffect, useState } from "react";
import { getRentals, returnItem } from "@/lib/api";
import RentalCard from "@/components/RentalCard";
import Link from "next/link";

type Rental = {
  id: number;
  itemName: string;
  rentedAt: string;
  status: string;
};

export default function RentalsPage() {
  const [rentals, setRentals] = useState<Rental[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError]     = useState(false);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) { window.location.href = "/auth/login"; return; }

    getRentals()
      .then(setRentals)
      .catch(() => setError(true))
      .finally(() => setLoading(false));
  }, []);

  const handleReturn = async (rental_id: number) => {
    try {
      await returnItem(rental_id);
      // Mettre à jour le status localement sans refetch
      setRentals(prev =>
        prev.map(r => r.id === rental_id ? { ...r, status: "returned" } : r)
      );
    } catch {
      alert("Failed to return item.");
    }
  };

  if (loading) return  (
    <main style={{ minHeight: "100vh", padding: "120px 40px 40px", background: "#0A0908" }}>
      <p style={{ color: "#C8B89A" }}>Loading...</p>
    </main>
  );
  if (error)   return  (
    <main style={{ minHeight: "100vh", padding: "120px 40px 40px", background: "#0A0908" }}>
      <p style={{ color: "#C8B89A" }}>Failed to load rentals.</p>
  </main>
  );

  return (
    <main style={{ minHeight: "100vh", padding: "120px 40px 40px", background: "#0A0908", fontFamily: "'Cormorant Garamond', serif" }}>
      <div className="flex items-center gap-4 mb-6">
        <Link href="/dashboard" className="text-yellow-600 underline text-sm">
          ← Back to Dashboard
        </Link>
        <h1 className="text-2xl font-bold">My Rentals</h1>
      </div>

      {rentals.length === 0 ? (
        <p className="text-gray-400">You have no rentals yet.</p>
      ) : (
        <div className="flex flex-col gap-4">
          {rentals.map((rental) => (
            <div key={rental.id} className="flex items-center justify-between">
              <RentalCard rental={rental} />
              {rental.status === "active" && (
                <button
                  onClick={() => handleReturn(rental.id)}
                  className="ml-4 px-4 py-2 bg-yellow-600 text-white rounded text-sm"
                >
                  Return
                </button>
              )}
            </div>
          ))}
        </div>
      )}
    </main>
  );
}