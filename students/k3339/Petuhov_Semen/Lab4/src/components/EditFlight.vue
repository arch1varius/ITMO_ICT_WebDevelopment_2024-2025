<template>
  <div class="modal-overlay">
    <div class="modal-content">
      <h3>Редактировать рейс</h3>
      <form @submit.prevent="saveFlight">
        <label for="flight_number">Номер рейса:</label>
        <input type="text" id="flight_number" v-model="form.flight_number" required />

        <label for="departure_date">Дата вылета:</label>
        <input type="datetime-local" id="departure_date" v-model="form.departure_date" required />

        <label for="arrival_date">Дата прилета:</label>
        <input type="datetime-local" id="arrival_date" v-model="form.arrival_date" required />

        <label for="status">Статус:</label>
        <select id="status" v-model="form.status" required>
          <option value="scheduled">Запланирован</option>
          <option value="delayed">Задержан</option>
          <option value="completed">Завершен</option>
        </select>

        <label for="onBoard_number">Номер на борту:</label>
        <input type="number" id="onBoard_number" v-model="form.onBoard_number" required />

        <label for="schedule_number">Номер расписания:</label>
        <input type="number" id="schedule_number" v-model="form.schedule_number" required />

        <button type="submit">Сохранить изменения</button>
        <button type="button" @click="close">Закрыть</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  props: ['flight'],
  data() {
    return {
      form: { ...this.flight }
    };
  },
  methods: {
    saveFlight() {
      this.$emit("save", this.form);
    },
    close() {
      this.$emit("close");
    }
  }
};
</script>

<style scoped>
/* Здесь можно добавить стили для модального окна */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  width: 400px;
}

button {
  background-color: #007bff;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
