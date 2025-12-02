import Day1 

main :: IO ()
main = do
    input <- readFile "input.txt"
    print (solve input)