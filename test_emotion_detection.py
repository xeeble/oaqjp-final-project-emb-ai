from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        
        '''
        Test label is equal for joy outcome
        '''
        self.assertEqual(emotion_detector('I am glad this happened')['dominant_emotion'], 'joy')
        
        '''
        Test label is equal for anger outcome
        '''
        self.assertEqual(emotion_detector('I am really mad about this')['dominant_emotion'], 'anger')
       
        '''
        Test label is equal for disgust outcome
        '''
        self.assertEqual(emotion_detector('I feel disgusted just hearing about this')['dominant_emotion'], 'disgust')      
    
        '''
        Test label is equal for sadness outcome
        '''
        self.assertEqual(emotion_detector('I am so sad about this')['dominant_emotion'], 'sadness')      
    
        '''
        Test label is equal for fear outcome
        '''
        self.assertEqual(emotion_detector('I am really afraid that this will happen')['dominant_emotion'], 'fear')      
    

unittest.main()