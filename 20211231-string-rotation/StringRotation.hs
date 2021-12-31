module StringRotation where

import Data.Text (isInfixOf, pack)

isStringRotation :: String -> String -> Bool
isStringRotation s1 s2 = areTheSameLength && s1 `isSubstringOf` (s2 <> s2)
  where
    areTheSameLength = length s1 == length s2

isSubstringOf :: String -> String -> Bool
isSubstringOf a b = pack a `isInfixOf` pack b
