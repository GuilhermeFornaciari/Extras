using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ChessProject.Entities
{
    public class Queen: ChessPiece
    {
        public Queen(int x, int y,string color) : base(x, y, color)
        {
        }

        public override string ToString()
        {
            if (Color == "W") return "Q";
            else return "q";
        }
    }
}
