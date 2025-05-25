
import React, { useState } from 'react';
import { StyleSheet, Text, View, TouchableOpacity, ActivityIndicator } from 'react-native';

export default function App() {
  const [status, setStatus] = useState("오늘의 낚시 결과는?");
  const [loading, setLoading] = useState(false);

  const fishes = ["금붕어", "참치", "돌고래", "신발", "물병", "황금 물고기"];

  const fish = () => {
    setLoading(true);
    setStatus("낚시 중...");
    setTimeout(() => {
      const caught = fishes[Math.floor(Math.random() * fishes.length)];
      setStatus(`${caught}를 낚았어요!`);
      setLoading(false);
    }, 2000 + Math.random() * 1000);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>{status}</Text>
      {loading && <ActivityIndicator size="large" color="#00f" />}
      <TouchableOpacity style={styles.button} onPress={fish} disabled={loading}>
        <Text style={styles.buttonText}>낚시하기!</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#cceeff',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20
  },
  title: {
    fontSize: 22,
    marginBottom: 20,
    fontWeight: 'bold'
  },
  button: {
    marginTop: 30,
    backgroundColor: '#0077cc',
    paddingVertical: 15,
    paddingHorizontal: 30,
    borderRadius: 10
  },
  buttonText: {
    color: '#fff',
    fontSize: 18
  }
});
