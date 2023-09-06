using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ChessProject.Entities
{
    public class Bishop: ChessPiece
    {
        public Bishop(int x, int y,string color) : base(x, y, color)
        {
        }

        public override string ToString()
        {
            if (Color == "W") return "B";
            else return "b";
        }
    }
}
