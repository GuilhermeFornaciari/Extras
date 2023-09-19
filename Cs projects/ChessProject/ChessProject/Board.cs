using ChessProject.Entities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ChessProject
{
    internal class Board
    {
        private object[,] _chessBoard;
        public object[,] ChessBoard { get { return _chessBoard; } set { _chessBoard = value; } }
        private string[] positionX { get; set; }
        private string[] positionY { get; set; }

        public Board()
        {

                       
            positionY = new String[] {"1", "2", "3", "4", "5", "6", "7", "8"};
            positionX = new String[] { "A", "B", "C", "D", "E", "F", "G", "H"};


            ChessBoard = new object[8, 8]
            {
                { new Rookie(0, 0, "W"), new Knight(0, 1, "W"),new Bishop(0, 2, "W"),new Queen(0, 3, "W"),new King(0, 4, "W"),new Bishop(0, 5, "W"),new Knight(0, 6, "W"),new Rookie(0, 7, "W")},
                { new Pawn(1, 0, "W"), new Pawn(1, 1, "W"), new Pawn(1, 2, "W"), new Pawn(1, 3, "W"), new Pawn(1, 4, "W"), new Pawn(1, 5, "W"), new Pawn(1, 6, "W"), new Pawn(1, 7, "W")},
                { new Empty(), new Empty(), new Empty(), new Empty(), new Empty(), new Empty(), new Empty(), new Empty()},
                { new Empty(), new Empty(), new Empty(), new Empty(), new Empty(), new Empty(), new Empty(), new Empty()},
                { new Empty(), new Empty(), new Empty(), new Empty(), new Empty(), new Empty(), new Empty(), new Empty()},
                { new Empty(), new Empty(), new Empty(), new Empty(), new Empty(), new Empty(), new Empty(), new Empty()},
                { new Pawn(1, 0, "B"), new Pawn(1, 1, "B"), new Pawn(1, 2, "B"), new Pawn(1, 3, "B"), new Pawn(1, 4, "B"), new Pawn(1, 5, "B"), new Pawn(1, 6, "B"), new Pawn(1, 7, "B")},
                { new Rookie(0, 0, "B"), new Knight(0, 1, "B"),new Bishop(0, 2, "B"),new King(0, 3, "B"),new Queen(0, 4, "B"),new Bishop(0, 5, "B"),new Knight(0, 6, "B"),new Rookie(0, 7, "B")},
            };

            





        }

        public void PrintBoard()
        {
            Console.Write("  ");
            for (int i = 0; i < ChessBoard.GetLength(1); i++)
            {
                Console.Write(positionX[i] + " ");
            }
            Console.WriteLine();


            for (int y = 0; y < ChessBoard.GetLength(0); y++)
            {
                Console.Write(positionY[y] + " ");
                for (int x = 0; x < ChessBoard.GetLength(1); x++)
                {
                    Console.Write(ChessBoard[y, x].ToString() + ",");
                }
                Console.WriteLine("");

            }

        }
    }
}
