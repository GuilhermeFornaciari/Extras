using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ChessProject.Entities
{
    public class King : ChessPiece
    {
        public King(int x, int y,string color) : base(x, y, color)
        {
        }

        public override string ToString()
        {
            if (Color == "W") return "K";
            else return "k";
        }
    }
}
