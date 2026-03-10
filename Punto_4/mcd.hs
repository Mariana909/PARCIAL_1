import System.CPUTime
import Text.Printf

mcd :: Int -> Int -> Int
mcd a 0 = a
mcd a b = mcd b (mod a b)

timeFunc :: IO a -> IO a
timeFunc action = do
    start  <- getCPUTime
    result <- action
    end    <- getCPUTime
    let diff = fromIntegral (end - start) / (10^12) :: Double
    printf "Tiempo de ejecución: %0.6f segundos\n" diff
    return result

main :: IO ()
main = do
    linea <- getLine
    let [a, b] = map read (words linea) :: [Int]
    resultado <- timeFunc $ do
        let r = mcd a b
        print r        -- fuerza evaluación lazy
        return r
    putStrLn $ "MCD(" ++ show a ++ ", " ++ show b ++ ") = " ++ show resultado
