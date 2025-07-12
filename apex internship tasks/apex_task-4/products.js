const products = [
  { name: "Headphones", category: "electronics", price: 120, rating: 4.5, image: "https://via.placeholder.com/200?text=Headphones" },
  { name: "T-Shirt", category: "clothing", price: 25, rating: 4.2, image: "https://via.placeholder.com/200?text=T-Shirt" },
  { name: "Smartphone", category: "electronics", price: 800, rating: 4.8, image: "https://via.placeholder.com/200?text=Smartphone" },
  { name: "Jacket", category: "clothing", price: 60, rating: 4.0, image: "https://via.placeholder.com/200?text=Jacket" },
  { name: "Laptop", category: "electronics", price: 1200, rating: 4.7, image: "https://via.placeholder.com/200?text=Laptop" },
];

const productGrid = document.getElementById("productGrid");
const categoryFilter = document.getElementById("categoryFilter");
const sortOption = document.getElementById("sortOption");

function displayProducts(list) {
  productGrid.innerHTML = "";
  list.forEach(product => {
    productGrid.innerHTML += `
      <div class="card">
        <img src="${product.image}" alt="${product.name}">
        <h3>${product.name}</h3>
        <p>Category: ${product.category}</p>
        <p>Price: $${product.price}</p>
        <p>Rating: ⭐ ${product.rating}</p>
      </div>
    `;
  });
}

function filterAndSortProducts() {
  let filtered = [...products];

  // Filter
  const selectedCategory = categoryFilter.value;
  if (selectedCategory !== "all") {
    filtered = filtered.filter(p => p.category === selectedCategory);
  }

  // Sort
  const selectedSort = sortOption.value;
  if (selectedSort === "priceLowHigh") {
    filtered.sort((a, b) => a.price - b.price);
  } else if (selectedSort === "priceHighLow") {
    filtered.sort((a, b) => b.price - a.price);
  } else if (selectedSort === "ratingHighLow") {
    filtered.sort((a, b) => b.rating - a.rating);
  }

  displayProducts(filtered);
}

// Initial display
displayProducts(products);

// Event listeners
categoryFilter.addEventListener("change", filterAndSortProducts);
sortOption.addEventListener("change", filterAndSortProducts);
