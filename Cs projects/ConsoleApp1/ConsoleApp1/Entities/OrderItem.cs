using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1.Entities
{
    internal class OrderItem
    {
        public float Quantity { get; set; }
        public double Price { get; set; }

        public Product Product { get; set; }

        public OrderItem(string name, double price,float quantity) 
        {
            Product = new Product(name,price);
            Quantity = quantity;
            Price = SubTotal();
        }  
        public OrderItem() { }
        private double SubTotal()
        {
            return Product.Price * Quantity;
        }
    }
}
