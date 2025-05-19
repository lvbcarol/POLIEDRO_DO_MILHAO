//esta tela é a tela do jogo que já está incluindo o back
import React, { useEffect, useState } from 'react';
import {
  TouchableOpacity,
  ImageBackground,
  View,
  Text,
  StyleSheet,
  useWindowDimensions,
  ScrollView,
  Image,
  Alert,
} from 'react-native';
import axios from 'axios';
import { useRouter } from 'expo-router';

type Pergunta = {
  id: number;
  pergunta: string;
  alternativas: string[];
  correta: string;
  dica: string;
};

const premios = [
  'R$ 0', 'R$ 1.000', 'R$ 5.000', 'R$ 10.000',
  'R$ 50.000', 'R$ 100.000', 'R$ 200.000',
  'R$ 400.000', 'R$ 600.000', 'R$ 800.000',
  'R$ 1.000.000'
];

export default function QuizScreen() {
  const router = useRouter();
  const { width } = useWindowDimensions();

  const [pergunta, setPergunta] = useState<Pergunta | null>(null);
  const [respostaSelecionada, setRespostaSelecionada] = useState<string | null>(null);
  const [perguntaAtual, setPerguntaAtual] = useState(0);
  const [ajudaUsada, setAjudaUsada] = useState({
    dica: false,
    menos2: false,
    pular: false,
  });
  const [eliminadas, setEliminadas] = useState<number[]>([]);

  const carregarPergunta = async () => {
    try {
      const response = await axios.get('http://10.0.2.2:5000/pergunta');
      setPergunta(response.data);
      setRespostaSelecionada(null);
      setEliminadas([]);
    } catch (error) {
      Alert.alert('Erro', 'Não foi possível carregar a pergunta.');
    }
  };

  const verificarResposta = async () => {
    if (!respostaSelecionada || !pergunta) return;

    try {
      const response = await axios.post('http://10.0.2.2:5000/verificar_resposta', {
        pergunta_id: pergunta.id,
        resposta: respostaSelecionada,
      });

      if (response.data.correto) {
        if (perguntaAtual === 9) {
          Alert.alert('Parabéns!', 'Você ganhou R$ 1.000.000!');
          router.push('/(tabs)/ScoreScreen');
        } else {
          setPerguntaAtual(perguntaAtual + 1);
          await carregarPergunta();
        }
      } else {
        Alert.alert('Fim de jogo', `Você errou! Ganhou ${premios[perguntaAtual]}`);
        router.push('/(tabs)/ScoreScreen');
      }
    } catch (error) {
      Alert.alert('Erro', 'Não foi possível verificar a resposta.');
    }
  };

  const usarDica = () => {
    if (ajudaUsada.dica || !pergunta) return;
    Alert.alert('Dica', pergunta.dica);
    setAjudaUsada({ ...ajudaUsada, dica: true });
  };

  const usarMenos2 = () => {
    if (ajudaUsada.menos2 || !pergunta) return;
    const incorretas = pergunta.alternativas
      .map((alt, idx) => ({ alt, idx }))
      .filter(a => a.alt !== pergunta.correta);
    const aRemover = incorretas.sort(() => 0.5 - Math.random()).slice(0, 2);
    setEliminadas(aRemover.map(a => a.idx));
    setAjudaUsada({ ...ajudaUsada, menos2: true });
  };

  const usarPular = async () => {
    if (ajudaUsada.pular) return;
    await carregarPergunta();
    setAjudaUsada({ ...ajudaUsada, pular: true });
  };

  const pararJogo = () => {
    Alert.alert('Jogo parado', `Você parou e ganhou ${premios[perguntaAtual]}`);
    router.push('/(tabs)/ScoreScreen');
  };

  useEffect(() => {
    carregarPergunta();
  }, []);

  return (
    <ScrollView contentContainerStyle={styles.scroll}>
      <ImageBackground
        source={require('../../../assets/images/TelaAzul.png')}
        style={styles.container}
        resizeMode="cover"
      >
        <View style={[styles.overlay, width > 768 && styles.overlayDesktop]}>
          {/* Cabeçalho */}
          <View style={styles.titleRow}>
            <Image source={require('../../../assets/images/Coin.png')} style={styles.coin} />
            <Text style={[styles.title, width > 768 && styles.titleDesktop]}>
              POLIEDRO{"\n"}DO MILHÃO
            </Text>
          </View>

          {/* Pergunta */}
          <View style={styles.questionContainer}>
            <Text style={styles.questionText}>{pergunta?.pergunta}</Text>

            <View style={styles.alternativesContainer}>
              {pergunta?.alternativas.map((alt, index) => (
                !eliminadas.includes(index) && (
                  <TouchableOpacity
                    key={index}
                    style={[
                      styles.alternativeButton,
                      respostaSelecionada === alt && { backgroundColor: '#ffa500' },
                    ]}
                    onPress={() => setRespostaSelecionada(alt)}
                  >
                    <Text style={styles.alternativeText}>{alt}</Text>
                  </TouchableOpacity>
                )
              ))}
              <TouchableOpacity
                onPress={verificarResposta}
                style={[styles.controlButton, { backgroundColor: '#0a5' }]}
              >
                <Text style={styles.controlText}>Confirmar</Text>
              </TouchableOpacity>
            </View>
          </View>

          {/* Rodapé */}
          <View style={styles.footer}>
            <Text style={styles.prizeText}>VALENDO {premios[perguntaAtual + 1]}</Text>

            <View style={styles.controlsRow}>
              <TouchableOpacity style={styles.controlButton} onPress={usarPular}>
                <Text style={styles.controlText}>Pular</Text>
              </TouchableOpacity>
              <TouchableOpacity style={styles.controlButton} onPress={usarMenos2}>
                <Text style={styles.controlText}>-2 Alternativas</Text>
              </TouchableOpacity>
              <TouchableOpacity style={styles.controlButton} onPress={pararJogo}>
                <Text style={styles.controlText}>Parar</Text>
              </TouchableOpacity>
              <TouchableOpacity style={styles.controlButton} onPress={usarDica}>
                <Text style={styles.controlText}>Dica</Text>
              </TouchableOpacity>
            </View>
          </View>
        </View>
      </ImageBackground>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  scroll: { flexGrow: 1 },
  container: { flex: 1, width: '100%', height: '100%' },
  overlay: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 20,
    paddingVertical: 40,
    backgroundColor: 'rgba(0, 0, 0, 0.4)',
  },
  overlayDesktop: { paddingHorizontal: 80 },
  titleRow: { flexDirection: 'row', alignItems: 'center', justifyContent: 'center' },
  coin: {
    width: 80, height: 80, resizeMode: 'contain',
    marginRight: 10,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    textAlign: 'center',
    color: '#FFD700',
  },
  titleDesktop: { fontSize: 28 },
  questionContainer: { width: '100%', alignItems: 'center', marginVertical: 30 },
  questionText: {
    fontSize: 22, fontWeight: 'bold', color: '#FFF', textAlign: 'center',
    marginBottom: 30,
    textShadowColor: 'rgba(0, 0, 0, 0.75)',
    textShadowOffset: { width: -1, height: 1 },
    textShadowRadius: 10,
  },
  alternativesContainer: { width: '100%', maxWidth: 600 },
  alternativeButton: {
    backgroundColor: '#5bbcc0',
    padding: 15,
    borderRadius: 10,
    marginVertical: 8,
    width: '100%',
  },
  alternativeText: {
    color: '#FFF',
    fontWeight: 'bold',
    fontSize: 16,
    textAlign: 'center',
  },
  footer: { width: '100%', alignItems: 'center' },
  prizeText: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#FFD700',
    marginBottom: 20,
    textShadowColor: 'rgba(0, 0, 0, 0.75)',
    textShadowOffset: { width: -1, height: 1 },
    textShadowRadius: 10,
  },
  controlsRow: {
    flexDirection: 'row',
    justifyContent: 'center',
    flexWrap: 'wrap',
    gap: 10,
  },
  controlButton: {
    backgroundColor: '#d5241c',
    paddingHorizontal: 15,
    paddingVertical: 10,
    borderRadius: 20,
    minWidth: 100,
    margin: 5,
  },
  controlText: {
    color: '#FFF',
    fontWeight: 'bold',
    textAlign: 'center',
  },
});
