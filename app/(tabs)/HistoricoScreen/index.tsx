import React from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, Image, ImageBackground } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { useRouter } from 'expo-router';

export default function HistoricoScreen() {
  const router = useRouter();

  return (
    <ImageBackground
      source={require('../../../assets/images/TelaVermelha.png')}
      style={styles.container}
      resizeMode="cover"
    >
      {/* Ícones superiores */}
      <TouchableOpacity style={styles.backIcon} onPress={() => router.push('../../../(tabs)/HomeScreen/')}>
        <Ionicons name="arrow-back" size={30} color="white" />
      </TouchableOpacity>

      <TouchableOpacity style={styles.soundIcon}>
        <Ionicons name="volume-high" size={30} color="white" />
      </TouchableOpacity>

      {/* Conteúdo principal com overlay */}
      <View style={styles.overlay}>
        {/* Cabeçalho */}
        <View style={styles.titleRow}>
          <Image source={require('../../../assets/images/Coin.png')} style={styles.coin} />
          <Text style={styles.title}>POLIEDRO{"\n"}DO MILHÃO</Text>
        </View>

        {/* Título da tela */}
        <Text style={styles.historyTitle}>HISTÓRICO</Text>

        {/* Bloco com tentativas */}
        <View style={styles.historyBox}>
          {/* Bolinhas superiores */}
          <View style={styles.bullets}>
            {Array.from({ length: 20 }).map((_, index) => (
              <View key={index} style={styles.bullet} />
            ))}
          </View>

          {/* Tentativas */}
          <View style={styles.attemptsBox}>
            <ScrollView>
              <Text style={styles.attemptText}>Tentativa 1: R$ 500.000,00</Text>
              <View style={styles.separator} />
              <Text style={styles.attemptText}>Tentativa 2: R$ 100.000,00</Text>
              <View style={styles.separator} />
              <Text style={styles.attemptText}>Tentativa 3: R$ 50.000,00</Text>
              {/* Adicione mais tentativas conforme necessário */}
            </ScrollView>
          </View>

          {/* Bolinhas inferiores */}
          <View style={styles.bullets}>
            {Array.from({ length: 20 }).map((_, index) => (
              <View key={index} style={styles.bullet} />
            ))}
          </View>
        </View>
      </View>
    </ImageBackground>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    width: '100%',
    height: '100%',
  },
  overlay: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal: 20,
    backgroundColor: 'rgba(0, 0, 0, 0.4)',
  },
  backIcon: {
    position: 'absolute',
    top: 40,
    left: 20,
    zIndex: 10,
  },
  soundIcon: {
    position: 'absolute',
    top: 40,
    right: 20,
    zIndex: 10,
  },
  titleRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
  },
  coin: {
    width: 80,
    height: 80,
    resizeMode: 'contain',
    marginBottom: 150,
    marginRight: 10,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    textAlign: 'center',
    color: '#FFD700',
    marginBottom: 150,
  },
  historyTitle: {
    fontSize: 20,
    color: '#FFD700',
    textAlign: 'center',
    marginBottom: 5,
  },
  historyBox: {
    width: '70%',
    backgroundColor: '#790000',
    borderRadius: 10,
    alignItems: 'center',
    paddingVertical: 5,
  },
  bullets: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'center',
    marginVertical: 8,
  },
  bullet: {
    width: 10,
    height: 10,
    borderRadius: 5,
    backgroundColor: '#FFD700',
    margin: 3,
  },
  attemptsBox: {
    backgroundColor: '#FFF',
    width: '90%',
    borderRadius: 5,
    padding: 10,
    maxHeight: 200,
  },
  attemptText: {
    fontSize: 16,
    marginVertical: 5,
  },
  separator: {
    height: 1,
    backgroundColor: '#ccc',
    marginVertical: 5,
  },
});
