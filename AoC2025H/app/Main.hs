--import Day1
--import Day2 
import Day7

printTable :: Show a => [a] -> IO ()
printTable [] = print()
printTable [line] = print $ show line
printTable (line:xs) = (print $ show line) >> printTable xs

main :: IO ()
main = do
    let path = (if False then "test" else "input") ++ "7.txt"
    input <- fmap lines (readFile path)
    let res = solve input
    --printTable $ snd $ res 
    print $ fst $ res