import { useState } from 'react'
import axios from './api/axios.js'
import './App.css'

const papersByDomain = {
  nlp: [
    "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers",
    "GPT-3: Language Models are Few-Shot Learners",
    "RoBERTa",
    "T5: Text-to-Text Transfer Transformer",
  ],
  computer_vision: [
    "ResNet",
    "YOLO",
    "Vision Transformer (ViT)",
    "Mask R-CNN",
    "EfficientNet",
  ],
  machine_learning: [
    "XGBoost",
    "Random Forests",
    "Support Vector Machines",
    "Gradient Boosting Machines",
    "AdaBoost",
  ],
  deep_learning: [
    "AlexNet",
    "VGGNet",
    "ResNet",
    "DenseNet",
    "InceptionNet",
  ],
  generative_ai: [
    "Stable Diffusion",
    "DALL·E",
    "StyleGAN",
    "Imagen",
    "DreamBooth",
  ],
  llm: [
    "GPT-4 Technical Report",
    "LLaMA",
    "PaLM",
    "Claude",
    "Gemini",
  ],
  reinforcement_learning: [
    "Deep Q-Network (DQN)",
    "AlphaGo",
    "Proximal Policy Optimization (PPO)",
    "A3C",
    "MuZero",
  ],
  multimodal_ai: [
    "CLIP",
    "Flamingo",
    "GPT-4V",
    "BLIP",
    "LLaVA",
  ],
  robotics: [
    "RT-2",
    "SayCan",
    "Diffusion Policy",
    "RoboCat",
    "Open X-Embodiment",
  ],
  ai_ethics: [
    "Fairness and Machine Learning",
    "Gender Shades",
    "Datasheets for Datasets",
    "Model Cards for Model Reporting",
  ],
  healthcare_ai: [
    "CheXNet",
    "Med-PaLM",
    "Deep Patient",
    "GatorTron",
  ],
  cybersecurity_ai: [
    "Malware Detection using Deep Learning",
    "AI for Intrusion Detection",
    "Graph-Based Cybersecurity Models",
  ],
  recommendation_systems: [
    "Wide & Deep Learning",
    "Neural Collaborative Filtering",
    "DeepFM",
    "BERT4Rec",
  ],
  speech_processing: [
    "Deep Speech",
    "wav2vec 2.0",
    "Whisper",
    "Tacotron 2",
  ],
  edge_ai: [
    "TinyML",
    "MobileNet",
    "EfficientNet-Lite",
    "MCUNet",
  ],
};
function App() {
  const [prompt, setPrompt] = useState("")
  const [error, setError] = useState("")
  const [showData, setData] = useState("")
  const [isLoading, setLoading] = useState(false)
  const [selectedAuthor, setAuthor] = useState("")
  const [selectedPaper, setPaper] = useState("")

  const onClickFunc = async () => {
    try {
      setLoading(true)
      console.log("praper-type ", selectedAuthor)
      console.log("paper ", selectedPaper)
      const res = await axios.post('/summary/', { 
        'paperType':selectedAuthor,
        'paper': selectedPaper
       })
      if (res.data.error) {
        setError(res.data.error)
      } else {
        setData(res.data.summary || JSON.stringify(res.data))
      }
    } catch (err) {
      setError(err.response?.data?.error || err.message || 'something went wrong')
    } finally {
      setLoading(false)
    }
  }

  return (
    <>
      <h3>Research Tool</h3>
      {error && <div>{error}</div>}
      {/* <input
        type="text"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter the prompt"
      /> */
      
      }
      <div style= {{padding : '20px'}}>
        <label htmlFor="options"> Choose an option</label>
        <select name="author" id="options" value={selectedAuthor} onChange = {(e) => {
          setAuthor(e.target.value)
        }} >
          <option value="" disabled selected>-- Select AI Research Paper Domain --</option>
          <option value="nlp">Natural Language Processing (NLP)</option>
          <option value="computer_vision">Computer Vision</option>
          <option value="machine_learning">Machine Learning</option>
          <option value="deep_learning">Deep Learning</option>
          <option value="generative_ai">Generative AI</option>
          <option value="llm">Large Language Models (LLMs)</option>
          <option value="reinforcement_learning">Reinforcement Learning</option>
          <option value="multimodal_ai">Multimodal AI</option>
          <option value="robotics">AI Robotics</option>
          <option value="ai_ethics">AI Ethics & Fairness</option>
          <option value="healthcare_ai">Healthcare AI</option>
          <option value="cybersecurity_ai">AI for Cybersecurity</option>
          <option value="recommendation_systems">Recommendation Systems</option>
          <option value="speech_processing">Speech & Audio Processing</option>
          <option value="edge_ai">Edge AI & TinyML</option>
          <option value="other">Other</option>
        </select>
      </div>
      <br />
      <div>
        <label htmlFor="paper-select"> Select Paper: </label>
        <select 
          id="paper-select" 
          value={selectedPaper} 
          disabled={!selectedAuthor}
          onChange={(e) => setPaper(e.target.value)}
        >
          {!selectedAuthor && <option value="">-- Select a domain first --</option>}
          {selectedAuthor &&
            papersByDomain[selectedAuthor]?.map((paperName, index) => (
              <option key={index} value={paperName}>
                {paperName}
              </option>
            ))}
        </select>
      </div>

      <div className='button-div'>
      <button onClick={onClickFunc} disabled={isLoading}>
        {isLoading ? 'Loading...' : 'Summarize'}
      </button>
      </div>
      <div className='show-data'>{showData}</div>
    </>
  )
}

export default App
