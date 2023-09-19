using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ChessProject.Entities
{
    public abstract class ChessPiece
    {
        public int X { get; set; }
        public int Y { get; set; }
        public string Color { get; set; }
        public ChessPiece(int x, int y, string color)
        {
            X = x; Y = y; Color = color;
        }
    }
}
