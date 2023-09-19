using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ChessProject.Entities
{
    public class Pawn:ChessPiece
    {
        public Pawn(int x, int y,string color) : base(x, y, color)
        {
        }

        public override string ToString()
        {
            if (Color == "W") return "P";
            else return "p";
        }
    }
}
