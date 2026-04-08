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
      <div className={`border rounded-xl p-4 hover:shadow-lg transition ${
        !item.available ? "opacity-50 cursor-not-allowed" : ""
      }`}>

        {item.images && item.images.length > 0 && (
          <img
            src={item.images[0]}
            alt={item.name}
            className="w-full h-48 object-cover rounded-lg mb-3"
          />
        )}

        <h2 className="font-bold text-lg">{item.name}</h2>
        <p className="text-gray-500">{item.brand} · Size {item.size}</p>
        <p className="text-purple-600 font-semibold">
          {item.price} MAD/month
        </p>

        <span className={`text-xs px-2 py-1 rounded-full mt-2 inline-block ${
          item.available
            ? "bg-green-100 text-green-700"
            : "bg-gray-100 text-gray-500"
        }`}>
          {item.available ? "Available" : "Rented"}
        </span>

      </div>
    </Link>
  );
}