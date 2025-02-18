class Application:
    def __init__(self, application_id, applicant, job, status):
        self.application_id = application_id
        self.applicant = applicant
        self.job = job
        self.status = status
    
    def save(self, db):
        db.execute('INSERT INTO application (id, applicant_id, job_id, status) VALUES (?, ?, ?, ?)',
                   (self.application_id, self.applicant.user_id, self.job.job_id, self.status))
    
    def delete(self, db):
        db.execute('DELETE FROM application WHERE id = ?', (self.application_id,))
    
    def update_status(self, db, status):
        db.execute('UPDATE application SET status = ? WHERE id = ?', (status, self.application_id))
