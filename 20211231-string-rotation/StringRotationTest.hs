import Control.Monad (void)
import StringRotation (isStringRotation)
import Test.HUnit
  ( Test (TestCase, TestList),
    assertEqual,
    runTestTT,
  )

main :: IO ()
main = void $ runTestTT $ TestList testCases

testCases :: [Test]
testCases =
  map
    testCase
    [ ("CodingInterview", "erviewCodingInt", True),
      ("CodingInt", "erviewCodingInt", False)
    ]

testCase :: (String, String, Bool) -> Test
testCase (a, b, expected) = TestCase (assertEqual label got expected)
  where
    label = a ++ " `isStringRotation` " ++ b
    got = a `isStringRotation` b
