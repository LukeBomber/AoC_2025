module Day1 where

import Text.Megaparsec
import Text.Megaparsec.Char
import Data.Void

type Parser = Parsec Void String
data Rotation = Rotation Char Int 
    deriving (Eq,Show)

pRotation :: Parser Rotation 
pRotation = (do 
    c <- oneOf "LR"
    n <- read <$> some digitChar 
    pure $ Rotation c n) <* optional space <* optional eol

pInput :: Parser [Rotation] 
pInput = many (pRotation)

rotate1 :: [Rotation] -> [Int] -> Int -> Int -> (Int,[Int])
rotate1 rots bookKeep current acc = 
    let newAcc = acc + fromEnum (current == 0)
    in
    case rots of 
        [] -> (newAcc, reverse (current:bookKeep))
        ((Rotation 'L' n):xs) -> 
            rotate1 xs (current:bookKeep) (mod (current-n) 100) newAcc
        ((Rotation 'R' n):xs) -> 
            rotate1 xs (current:bookKeep) (mod (current+n) 100) newAcc
        _ -> error "This should be unreachable"

rotate2 :: [Rotation] -> [Int] -> Int -> Int -> (Int,[Int])
rotate2 rots bookKeep current acc = 
    let newAcc = acc 
    in 
    case rots of 
        [] -> (newAcc, reverse bookKeep)
        ((Rotation 'L' n):xs) ->
            let cnt = abs((div (current-n) 100)) - fromEnum (current==0) + fromEnum ((mod (current-n) 100)==0)
            in rotate2 xs ((-cnt):bookKeep) (mod (current-n) 100) (newAcc+cnt)
        ((Rotation 'R' n):xs) -> 
            let cnt = div (current+n) 100 
            in rotate2 xs (cnt:bookKeep) (mod (current+n) 100) (newAcc+cnt)
        _ -> error "This should be unreachable"

solve :: String -> (Int, [Int])--((Int, [Int]), Int)
solve input = 
    case runParser pInput "input" input of 
        Left _ -> undefined
        --Right xs -> (rotate1 xs [] 50 0)
        Right xs -> (rotate2 xs [] 50 0)--((rotate xs [] 50 0),length xs) 
